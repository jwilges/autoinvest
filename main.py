#!/usr/bin/env python

from __future__ import print_function
from structures import OwnedNote, ListedLoan
import configuration
import json, sys, urllib2

# GET
# Authorization: {token}
# Accept: application/json
# POST
# Authorization: {token}
# Accept: application/json
# Content-type : application/json

def restGetResponse(url, data=None, headers=None, timeout=None):
    request = urllib2.Request(url, data, headers)
    if timeout:
        return urllib2.urlopen(request, timeout=timeout)
    else:
        return urllib2.urlopen(request)

def queryOwnedNotes():
    OWNED_NOTES_BASE_URL = "https://api.lendingclub.com/api/investor/{version}/accounts/{investorId}/detailednotes"
    queryUrl = OWNED_NOTES_BASE_URL.format(**{"version": "v1", "investorId": configuration.API_INVESTOR_ID})
    queryHeaders = {
        "Authorization": configuration.API_AUTHORIZATION_TOKEN,
        "Accept": "application/json"
    }
    queryResponse = restGetResponse(queryUrl, headers=queryHeaders)
    return json.load(queryResponse)

def getOwnedNotesList():
    ownedNotesResult = queryOwnedNotes()
    ownedNotes = []
    for ownedNote in ownedNotesResult["myNotes"]:
        ownedNotes.append(OwnedNote(ownedNote))
    return ownedNotes

def queryListedLoans():
    LOANS_BASE_URL = "https://api.lendingclub.com/api/investor/{version}/loans/listing"
    loansUrl = LOANS_BASE_URL.format(**{"version": "v1"})
    loansHeaders = {
        "Authorization": configuration.API_AUTHORIZATION_TOKEN,
        "Accept": "application/json"
    }
    loansResponse = restGetResponse(loansUrl, headers=loansHeaders)
    return json.load(loansResponse)

def main():
    listedLoansResult = queryListedLoans()

    queryDate = listedLoansResult["asOfDate"]
    if queryDate is None:
        print("error: invalid/missing asOfDate", file=sys.stderr)
        sys.exit(1)

    print("Query Date: {0}".format(queryDate))
    listedLoans = []
    for listedLoan in listedLoansResult["loans"]:
        newListedLoan = ListedLoan(listedLoan)
        if configuration.BaseLoanFilter(newListedLoan):
            print(newListedLoan)
            print("  grade: {0}; subgrade: {1}".format(newListedLoan.Grade, newListedLoan.SubGrade))
            print("  credit balance (no mtg): {0}; (with): {1}".format(newListedLoan.TotalCreditBalanceExcludingMortgage, newListedLoan.RevolvingCreditBalance))
            print("  all balance: {0}".format(newListedLoan.TotalCurrentBalance))
            print("  title: {0} ({1:.2f} years)".format(newListedLoan.EmploymentTitle, newListedLoan.EmploymentLength / 12.0))
            print("  since record: {0}; since delinquency: {1}".format(newListedLoan.MonthsSinceLastRecord, newListedLoan.MonthsSinceLastDelinquency))
            listedLoans.append(newListedLoan)

if __name__ == "__main__":
    main()
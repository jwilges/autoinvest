#!/usr/bin/env python

from __future__ import print_function
from structures import Loan
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

def getLoans(token):
    LOANS_BASE_URL = "https://api.lendingclub.com/api/investor/{version}/loans/listing"
    loansUrl = LOANS_BASE_URL.format(**{"version": "v1"})
    loansHeaders = {
        "Authorization": token,
        "Accept": "application/json"
    }
    loansResponse = restGetResponse(loansUrl, headers=loansHeaders)
    return json.load(loansResponse)

def main():
    loansResult = getLoans(configuration.API_AUTHORIZATION_TOKEN)

    queryDate = loansResult["asOfDate"]
    if queryDate is None:
        print("error: invalid/missing asOfDate", file=sys.stderr)
        sys.exit(1)

    print("Query Date: {0}".format(queryDate))
    loans = []
    for loan in loansResult["loans"]:
        newLoan = Loan(loan)
        if configuration.BaseLoanFilter(newLoan):
            print(newLoan)
            print("  grade: {0}; subgrade: {1}".format(newLoan.Grade, newLoan.SubGrade))
            print("  credit balance (no mtg): {0}; (with): {1}".format(newLoan.TotalCreditBalanceExcludingMortgage, newLoan.RevolvingCreditBalance))
            print("  all balance: {0}".format(newLoan.TotalCurrentBalance))
            print("  title: {0} ({1:.2f} years)".format(newLoan.EmploymentTitle, newLoan.EmploymentLength / 12.0))
        loans.append(newLoan)

if __name__ == "__main__":
    main()
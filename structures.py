class Loan(object):
    def __init__(self, data):
        self.Id = data["id"]
        self.MemberId = data["memberId"]
        self.Term = data["term"]
        self.InterestRate = data["intRate"]
        self.ExpectedDefaultRate = data["expDefaultRate"]
        self.ServiceFeeRate = data["serviceFeeRate"]
        self.Installment = data["installment"]
        self.Grade = data["grade"]
        self.SubGrade = data["subGrade"]
        self.EmploymentLength = data["empLength"] if data["empLength"] is not None else 0.0
        self.EmploymentTitle = data["empTitle"]
        self.HomeOwnership = data["homeOwnership"]
        self.AnnualIncome = data["annualInc"]
        self.IsIncomeVerified = data["isIncV"]
        self.AcceptDate = data["acceptD"]
        self.ExpirationDate = data["expD"]
        self.ListDate = data["listD"]
        self.CreditPullDate = data["creditPullD"]
        self.ReviewStatusDate = data["reviewStatusD"]
        self.ReviewStatus = data["reviewStatus"]
        self.Description = data["desc"]
        self.Purpose = data["purpose"]
        self.AddressZip = data["addrZip"]
        self.AddressState = data["addrState"]
        self.InvestorCount = data["investorCount"]
        self.InitialListStatusExpirationDate = data["ilsExpD"]
        self.InitialListStatus = data["initialListStatus"]
        self.AccountsNowDelinquent = data["accNowDelinq"]
        self.AccountsOpenPast24Months = data["accOpenPast24Mths"]
        self.BankCardsOpenToBuy = data["bcOpenToBuy"]
        self.PercentBankCardsGreaterThan75 = data["percentBcGt75"]
        self.BankCardUtilization = data["bcUtil"]
        self.DebtToIncome = data["dti"]
        self.Delinquent2Years = data["delinq2Yrs"]
        self.DelinquentAmount = data["delinqAmnt"]
        self.EarliestCreditLine = data["earliestCrLine"]
        self.FicoRangeLow = data["ficoRangeLow"]
        self.FicoRangeHigh = data["ficoRangeHigh"]
        self.InqueriesWithin6Months = data["inqLast6Mths"]
        self.MonthsSinceLastDelinquency = data["mthsSinceLastDelinq"]
        self.MonthsSinceLastRecord = data["mthsSinceLastRecord"]
        self.MonthsSinceRecentInquery = data["mthsSinceRecentInq"]
        self.MonthsSinceRecentRevolvingDelinquency = data["mthsSinceRecentRevolDelinq"]
        self.MonthsSinceRecentBankCard = data["mthsSinceRecentBc"]
        self.MortgageAccounts = data["mortAcc"]
        self.OpenCreditAccounts = data["openAcc"]
        self.DerogatoryPublicRecords = data["pubRec"]
        self.TotalCreditBalanceExcludingMortgage = data["totalBalExMort"]
        self.RevolvingCreditBalance = data["revolBal"]
        self.RevolvingUtilization = data["revolUtil"]
        self.TotalBankCardLimit = data["totalBcLimit"]
        self.TotalCreditAccounts = data["totalAcc"]
        self.TotalInstallmentHighCreditLimit = data["totalIlHighCreditLimit"]
        self.RevolvingAccounts = data["numRevAccts"]
        self.MonthsSinceRecentBankCardDelinquency = data["mthsSinceRecentBcDlq"]
        self.PublicRecordBankruptcies = data["pubRecBankruptcies"]
        self.AccountsEver120DaysPastDue = data["numAcctsEver120Ppd"]
        self.ChargeoffsWithin12Months = data["chargeoffWithin12Mths"] # stopped renaming here
        self.CollectionsWithin12MonthsExcludingMedical = data["collections12MthsExMed"]
        self.TaxLiens = data["taxLiens"]
        self.MthsSinceLastMajorDerog = data["mthsSinceLastMajorDerog"]
        self.NumSats = data["numSats"]
        self.NumTlOpPast12m = data["numTlOpPast12m"]
        self.MoSinRcntTl = data["moSinRcntTl"]
        self.TotHiCredLim = data["totHiCredLim"]
        self.TotalCurrentBalance = data["totCurBal"]
        self.AverageCurrentBalance = data["avgCurBal"]
        self.BankCardAccounts = data["numBcTl"]
        self.ActiveBankCardAccounts = data["numActvBcTl"]
        self.SatisfactoryBankCardAccounts = data["numBcSats"]
        self.PctTlNvrDlq = data["pctTlNvrDlq"]
        self.NumTl90gDpd24m = data["numTl90gDpd24m"]
        self.NumTl30dpd = data["numTl30dpd"]
        self.NumTl120dpd2m = data["numTl120dpd2m"]
        self.NumIlTl = data["numIlTl"]
        self.MoSinOldIlAcct = data["moSinOldIlAcct"]
        self.NumActvRevTl = data["numActvRevTl"]
        self.MoSinOldRevTlOp = data["moSinOldRevTlOp"]
        self.MoSinRcntRevTlOp = data["moSinRcntRevTlOp"]
        self.TotalRevHiLim = data["totalRevHiLim"]
        self.NumRevTlBalGt0 = data["numRevTlBalGt0"]
        self.NumOpRevTl = data["numOpRevTl"]
        self.CollectionsAmountsOwed = data["totCollAmt"]
        self.FundedAmount = data["fundedAmount"]
        self.LoanAmount = data["loanAmount"]

    def __str__(self):
        return "id: {id}; member id: {memberId}; amount: {loanAmount}".format(**{"id": self.Id, "memberId": self.MemberId, "loanAmount": self.LoanAmount})

    def __repr__(self):
        return "<Loan: {0}>".format(str(self))
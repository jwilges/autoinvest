from structures import LoanPurpose

API_AUTHORIZATION_TOKEN = ""
API_INVESTOR_ID = 0

EMPLOYMENT_TITLE_BLACKLIST = (
    "owner",
    "proprietor",
    "chief executive officer",
    "ceo",
    "chief financial officer",
    "cfo",
    "chief technical officer",
    "cto"
)

def BaseLoanFilter(loan):
    return loan.LoanAmount <= 30000.00 and \
           loan.LoanAmount <= (loan.RevolvingCreditBalance + 1000.0) and \
           loan.CollectionsWithin12MonthsExcludingMedical == 0 and \
           loan.AnnualIncome >= 55000.0 and \
           loan.InqueriesWithin6Months == 0 and \
           loan.DerogatoryPublicRecords == 0 and \
           loan.RevolvingCreditBalance < 75000.0 and \
           (loan.MonthsSinceLastDelinquency is None or loan.MonthsSinceLastDelinquency >= 60) and \
           (loan.MonthsSinceLastRecord is None or loan.MonthsSinceLastRecord >= 60) and \
           loan.EmploymentLength >= 24.0 and \
           loan.EmploymentTitle is not None and \
           loan.EmploymentTitle.lower() not in EMPLOYMENT_TITLE_BLACKLIST and \
           loan.AddressState not in ("CA", "FL", "NV", "NY") and \
           loan.Grade in ("B", "C", "D", "E") and \
           loan.HomeOwnership in ("OWN", "MORTGAGE") and \
           loan.Purpose in (LoanPurpose.DebtConsolidation, LoanPurpose.HomeImprovement, LoanPurpose.Wedding, LoanPurpose.House, LoanPurpose.CreditCard)
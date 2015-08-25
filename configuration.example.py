API_AUTHORIZATION_TOKEN = ""

def BaseLoanFilter(loan):
    return loan.LoanAmount <= 30000.00 and \
           loan.InqueriesWithin6Months == 0 and \
           loan.CollectionsWithin12MonthsExcludingMedical == 0 and \
           loan.Grade in ("B", "C", "D", "E") and \
           loan.HomeOwnership == "OWN" and \
           loan.EmploymentTitle is not None and \
           loan.EmploymentLength >= 24.0
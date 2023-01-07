#if applicant has high income or good credit: Eligible for loan
has_good_credit=False
has_high_income=True
if has_good_credit or has_high_income: # atleast one condition must be ture
    print("ELigible for loan")
else:
    print("Not eligible for loan")
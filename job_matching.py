from fuzzywuzzy import fuzz

def job_matching(resume_text, job_description):
    score = fuzz.token_sort_ratio(resume_text, job_description)
    return score

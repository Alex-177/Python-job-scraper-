from headhunter import get_jobs as hh_get_jobs
from so import get_jobs as so_get_jobs
from save import savetocsv


hh_jobs=hh_get_jobs()
so_jobs = so_get_jobs()

jobs = hh_jobs + so_jobs


savetocsv(jobs)



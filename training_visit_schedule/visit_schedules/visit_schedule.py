from edc_visit_schedule import VisitSchedule, site_visit_schedules
from .schedule import training_subject_visit_schedule

visit_schedule = VisitSchedule(
    name='subject_visit_schedule',
    verbose_name='Training',
    offstudy_model='training_prn.subjectoffstudy',
    locator_model='training_subject.personalcontactinfo',
    death_report_model='training_prn.deathreport',
    previous_visit_schedule=None)

visit_schedule.add_schedule(training_subject_visit_schedule)


site_visit_schedules.register(visit_schedule)

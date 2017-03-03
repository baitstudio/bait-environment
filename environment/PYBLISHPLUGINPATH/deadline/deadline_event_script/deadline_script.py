import os
import sys


def main():

    job_status = sys.argv[0]
    job = sys.argv[1]

    # Setup environment from job.
    if job.GetJobEnvironmentKeys():
        for key in job.GetJobEnvironmentKeys():
            value = job.GetJobEnvironmentKeyValue(key)
            os.environ[str(key)] = str(value)

    status_mapping = {
        "OnJobSubmitted": "Render",
        "OnJobStarted": "Render",
        "OnJobFinished": "Artist Review",
        "OnJobRequeued": "Render",
        "OnJobFailed": "Render Failed",
        "OnJobSuspended": "Render",
        "OnJobResumed": "Render",
        "OnJobPended": "Render",
        "OnJobReleased": "Render",
    }

    # Fail safe for non-existing job statuses
    if job_status not in status_mapping.keys():
        return

    # Need to find the status by name
    sys.path.append(job.GetJobEnvironmentKeyValue("PYTHONPATH"))

    import ftrack

    ft_status = None
    for status in ftrack.getTaskStatuses():
        if status.getName() == status_mapping[job_status]:
            ft_status = status
            break

    task = ftrack.Task(job.GetJobEnvironmentKeyValue("FTRACK_TASKID"))
    task.setStatus(ft_status)
    print "Setting \"{0}\" to \"{1}\"".format(
        task.getName(), ft_status.getName()
    )


main()

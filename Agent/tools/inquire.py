from zhipuai import ZhipuAI

client = ZhipuAI(api_key="4a478b99108ee30c1ae4aaa0aefe6632.X8sj7A6gaBgWh9AE")

fine_tuning_job = client.fine_tuning.jobs.retrieve(
    fine_tuning_job_id = "ftjob-20240814145733803-pq7jg" ,
)
print(fine_tuning_job)
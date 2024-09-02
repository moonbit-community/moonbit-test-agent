from zhipuai import ZhipuAI

client = ZhipuAI(api_key="4a478b99108ee30c1ae4aaa0aefe6632.X8sj7A6gaBgWh9AE")

job = client.fine_tuning.jobs.create(
    model="glm-4-9b",
    training_file="file-20240814014955141-bpp67",
    hyperparameters={"n_epochs": 5},
    suffix="v1"
)
job_id = job.id

print(job_id)
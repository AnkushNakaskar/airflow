import json
import pathlib
import airflow
import requests
import requests.exceptions as requests_exceptions
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

def get_pictures():
    pathlib.Path("/tmp/images").mkdir(parents=True, exist_ok=True)
    with open("/tmp/images") as f:
        launches = json.load(f)
        image_urls = [launch["image"] for launch in launches["results"]]
        for image_url in image_urls:
            try:
                response =requests.get(image_url);
                image_filename = image_url.split("/")[-1]
                target_file = f"/tmp/images/{image_filename}"
                with open(target_file, "wb") as f:
                    f.write(response.content)
                print(f"Downloaded {image_url} to {target_file}")
            except:
                print("Image url apear to be invalid URL")


with DAG(dag_id="rocket_launcher_book_example",start_date=airflow.utils.dates.days_ago(14),schedule_interval=None) as dag:
    download_launches =BashOperator("download_launches",bash_command="curl -o /tmp/launches.json -L 'https://ll.thespacedevs.com/2.0.0/launch/upcoming'");
    get_pictures = PythonOperator(task_id="get_pictures", python_callable=get_pictures)
    notify = BashOperator(task_id="notify",bash_command='echo "There are now $(ls /tmp/images/ | wc -l) images."')
download_launches >> get_pictures >> notify

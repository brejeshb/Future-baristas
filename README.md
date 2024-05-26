# Future-baristas

Project Description for submission

Social Responsibility
The solution is a website built on django which registers volunteers and volunteer organisations. Once registered, volunteers linkedIn will be scraped using Jigsaw stack AI scraper (not implemented due to LinkedIn API key limitations ) for their skills from their LinkedIn URL that they provide upon registration. Volunteers can view a dashboard of relevant volunteer postings by organisations. Organisations can put up postings with an AI generated story (OpenAI API) to illustrate their cause. The solution targets skilled professionals namely on LinkedIn


1. Navigate to your project directory:
```
cd path\to\your\project
```

3. Create a virtual environment:
   
```
python -m venv venv_name
```

5. Activate the virtual environment:

On Windows:
```
.\venv_name\Scripts\Activate
```

On macOS and Linux:

```
source venv_name/bin/activate
```

Install the required dependencies:

```
pip install django
```

Running the Project
After setting up the environment, you can run the project with the following command:

```
python manage.py runserver
```
This command will start the development server. You can access the application in your web browser at http://127.0.0.1:8000/.

# Bias Analysis Website

## Description

### What it does
This site uses OpenAI's API to give a linked URL a site bias score along with a brief description on why the score was given.

### Tech used
Flask, Python, OpenAI API, HTML

### Challenges faced

Started with Django but many of its features were uneccesary for this project and was more time consuming to learn. For this reason, I switched to Flask and had to learn how it works as well as how html works in order to display the information. Finally, I was unable to host the project on GitHub pages as pages does not support web apps and is only built for static html. 


### Future feature implementation

Hosting web app on Google App Engine

Add option for local ollama and homemade models rather than just OpenAI models

Improving UI to show the article linked and mention specific examples in each response.

**Proof of concept:**
![BCORE_PROJ](https://github.com/ManuelBX/bias-website/assets/91144975/f2fd07ed-64a8-45d3-a0c8-c892285b4fd0)

## Using the site locally
Clone github repository

Install Python 3.9 or higher

Install the flask and openai libraries by running the following commands
```
python -m pip install --upgrade pip
pip install flask openai
```

Create file OPENAI_API_KEY.env with your own project key
or
Replace client line 6-8 with:
```
os.environ["OPENAI_API_KEY"] = "YOUR_KEY_HERE"
client = OpenAI()
```
Alternatively you can set the project key globally on your machine by following this comment
https://community.openai.com/t/open-ai-error-key-not-found/15577/2 

Then, run the website locally by running the following command in your terminal
```
flask --app app run
```

Finally, click the port that it was opened on (usually http://127.0.0.1:5000) and use the website!

Optionally, you can experiment with different OpenAI models by replacing the line in the response call
```
model="gpt-3.5-turbo"
```
with any of the models mentioned in the documentation (https://platform.openai.com/docs/models)

### Credits
Manuel Braje

### License
MIT License
Copyright 2024 Manuel Braje

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

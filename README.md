# linkedin-post

It uploads the post on your LinkedIn profile via LinkedIn API.

### Steps to run script 
1. Install the requirements using pip as `pip install -r requirements.txt`.
2. Create an app on LinkedIn's developers account [here](https://www.linkedin.com/developers/) and follow the guide [here](https://docs.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?context=linkedin/context) to get the access token. After getting access token, send a `GET` request defined [here](https://docs.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/sign-in-with-linkedin?context=linkedin/consumer/context#api-request) to get the Person `URN` from the response.
3. Create a `.env` file and write the follwing content into it
```
ACCESS_TOKEN="<your access token>"
URN="<your urn>"
```
4. Run the script using `python post_on_linkedin.py` which will print the `SUCCESS` and `id` of the post shared as a JSON response. You can now check as well on your LinkedIn profile. :)

### License
This code is available with [MIT](https://github.com/gutsytechster/linkedin-post/blob/master/LICENSE) License

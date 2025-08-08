# document-translation-agent-ibm

This repo holds the code for a document translation project using watsonx.ai and watsonx Orchestrate ADK.

1. For the AI Service portion, I used Watson Studio within watsonx.ai. To recreate, you can import `document_translation_v3_ai_service.ipynb`. You will need to create a project in your watsonx.ai environment where you can then upload this notebook. There are a number of keys and connections required throughout the notebook (COS, Runtime, deployment space, ...).

2. Install the [watsonx Orchestrate ADK](https://developer.watson-orchestrate.ibm.com/getting_started/wxOde_setup) (if you don't already have). Like the installation instructions mention, set up a `.env` file in the directory you are working in.

    ```
    WO_DEVELOPER_EDITION_SOURCE=myibm
    WO_ENTITLEMENT_KEY= <your entitlement key>
    WATSONX_APIKEY= <your api key>
    WATSONX_SPACE_ID= <your space id>
    WO_DEVELOPER_EDITION_SKIP_LOGIN=false
    ```

3. (Optional) To ensure everything is set up and running smoothly, I recommend following this [tutorial](https://developer.watson-orchestrate.ibm.com/tutorials/tutorial_1_hello_world). The files are in the `helloworld` folder.

   You will likely need to use these commands:
   - Start a local server instance: `orchestrate server start --env-file={{The path of your .env file}}`
   - Activate the local environment: `orchestrate env activate local`
   - (If you aren't already, navigate to the `helloworld` directory) Create the `greetings` tool: `orchestrate tools import -k python -f tools/greetings.py`
   - Create the `greeter` agent: `orchestrate agents import -f greeter.yaml`
   - Start the chat in the local host: `orchestrate chat start`
   - Play around in the UI. If you type "Greeting", the agent should respond with "Hello World"

4. Create the document translation agent. The steps are similiar to the greeter agent above. Download the files to your directory. Create the tools and agent. Start chatting.

   ```
   orchestrate server start --env-file=./.env
   orchestrate env activate local
   orchestrate tools import -k python -f tools/document_translation_v3.py
   orchestrate tools import -k python -f tools/content_extraction.py -r requirements.txt
   orchestrate agents import -f document_translation_v3.yaml
   orchestrate chat start
   ```

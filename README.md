# How to use ChatGPT from terminal using Python

1. If you are not already registered you need to go to: https://chat.openai.com/chat and register.

<br>

2. If you are registered and logged in, got to: https://platform.openai.com/account/api-keys to get your API-KEY.

<br>

3. Next, you need to set your API-KEY as global variable, using:
    ```bash
    echo 'export OPENAI_API_KEY=<your-openAi-API-KEY>' >> ~/.bashrc 
    ```
    instead of the last command you could use your API-KEY directly inside the `openAi.py` by typing this line at the top of your script:

    `openai.api_key = "<your-openAi-API-KEY>"`

<br>

4. The next step is to install the openAi python module, using:
    ```bash
    pip install openai
    ```

<br>

5. Now view/modify the `openAi.py` script if you want (optional).

<br>

6. For ease of use I also added an alias to my `.bash_aliases` (optional)
    ```bash
    echo "alias askAi='python3 ~/path/to/script/openAi.py'" >> ~/.bash_aliases
    ```
<br>

7. Source your terminal, using:
    ```bash
    source ~/.bashrc
    ```
<br>

8. Finally you can run the program, using:
    ```bash
    askAi
    ```
    You can end the program by typing:
    ```bash
    end
    ```

<br>

You can also check out:

https://platform.openai.com/docs/models/gpt-3

and tweak your python script e.g. using other language models.

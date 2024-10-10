## WATERMARK FOR LARGE PDF'S
- A simple python based watermark adder for large pdf's
  - To try , do the following :
  - Clone the repo

    ```
      git clone https://github.com/adiboy-23/watermark-for-large-pdf.git
    ```

  - install PyPDF2 and reportlab locally either by making a virtual env(Linux and Mac) or directly(Windows users)
    
    - Virtual environment
          
            python3 -m venv <vir_env_name>
            source ./<vir_env_name>/bin/activate
            pip install PyPDF2
            pip install reportlab
          
          
        - Locally in windows
          
          ```
            pip install PyPDF2
            pip install reportlab
          ```

        - to start the process , first make the watermark.pdf(change the watermark name) file by doing the below
          
          ```
            python watermark.py
          ```

      - secondly run the main.py file(change the original pdf location
        ```
            python main.py
        ```

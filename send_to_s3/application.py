
from flask import Flask, render_template, request
import boto3
application = Flask(__name__)
from werkzeug.utils import secure_filename
#import key_config as keys

s3 = boto3.client('s3',
                    aws_access_key_id="AKIA2M2VVMTUVIQZOC47",
                    aws_secret_access_key= "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"
                    # aws_session_token=keys.AWS_SESSION_TOKEN
                     )

BUCKET_NAME='wellwater'

@application.route('/')  
def home():
    return render_template("file_upload_to_s3.html")

@application.route('/upload',methods=['post'])
def upload():
    if request.method == 'POST':
        img = request.files['file']
        if img:
                filename = secure_filename(img.filename)
                img.save(filename)
                s3.upload_file(
                    Bucket = BUCKET_NAME,
                    Filename=filename,
                    Key = filename
                )
                msg = "Upload Done ! "

    return render_template("file_upload_to_s3.html",msg =msg)




if __name__ == "__main__":
    
    application.run(debug=True, port=3000)



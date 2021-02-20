from flask import Flask, render_template, redirect, request
import gpt_2_simple as gpt

app = Flask(__name__)
sess = None
model_loaded = False

@app.route('/')
def index():
    return render_template('index.html', model_loaded=model_loaded)

@app.route('/load-model')
def load():
    global sess
    global model_loaded
    # sess = gpt.start_tf_sess()
    # gpt.load_gpt2(sess)
    model_loaded = True
    return redirect('/')

@app.route('/generate', methods=['GET', 'POST'])
def gen():
    if request.method == 'POST':
        dets = request.form
        dream = dets['dream']
        length = int(dets['length'])
        res = dream, length
        # res = gpt.generate(sess, length=length, prefix=dream, temperature=0.7, run_name='run1', include_prefix=False, nsamples=3, return_as_list=True)
        return render_template('generate.html', text=res)

if __name__ == '__main__':
    app.run(debug=True)
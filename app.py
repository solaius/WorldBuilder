from flask import Flask, render_template, request

from WB_Setting_Creator import setting_elements
from WB_Setting_Creator import submit_setting

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/settingbuilder')
def settingbuilder():
    return render_template('SettingBuilder.html', setting_elements=setting_elements)

@app.route('/settingbuilder', methods=['POST'])
def Submit_Setting():
    setting_name = request.form.get('setting-name')
    setting_type = request.form.get('setting-types')
    setting_subtype = request.form.get('setting-subtypes')
    setting_tone = request.form.get('setting-tones')
    setting_size = request.form.get('setting-size')
    setting_description = request.form.get('setting-description')
    negative_description = request.form.get('negative-description')
    submit_setting(setting_name, setting_type, setting_subtype, setting_tone, setting_size, setting_description, negative_description)
    return render_template('SettingBuilder.html', setting_elements=setting_elements)

@app.route('/worldbuilder')
def worldbuilder():
    return render_template('test.html', setting_elements=setting_elements)

@app.route('/citybuilder')
def citybuilder():
    return render_template('CityBuilder.html', setting_elements=setting_elements)

@app.route('/npcbuilder')
def npcbuilder():
    return render_template('NPCBuilder.html', setting_elements=setting_elements)

@app.route('/characterbuilder')
def characterbuilder():
    return render_template('CharacterBuilder.html', setting_elements=setting_elements)

@app.route('/encounterbuilder')
def encounterbuilder():
    return render_template('EncounterBuilder.html', setting_elements=setting_elements)

if __name__ == '__main__':
    app.run(debug=True)
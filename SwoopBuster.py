from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
import subprocess

def run_command_line_tool(website, hitList="checklist.txt", results="results.txt", engine="gobuster_Windows_i386", type="dir"):
    try:
        # dns and dir have different -u -d requirements
        if(type == "dns"):
            type = "dns -d"
        elif(type == "dir"):
            type = "dir -u"

        # Build the command
        command = f"./gobuster/{engine}/gobuster {type} https://{website} -w {hitList} -o {results}"

        print(command)
        command_args = command

        # Run the command and capture the output
        result = subprocess.run(command_args, text=True, capture_output=True)

        # Print the output of the command
        print("Command output:")
        print(result.stdout)

        # Check for errors
        if result.returncode != 0:
            print("Error executing the command. Exit code:", result.returncode)
            print("Error message:")
            print(result.stderr)

        return result.stdout
    except Exception as e:
        print("An error occurred:", str(e))
        return None

def domain_simplify(text):
    domain = text
    return domain

class MyApp(App):
    def build(self):
        # Create a BoxLayout as the root widget
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        layoutTop = BoxLayout(orientation='horizontal', spacing=10, padding=10)

        # Create a TextInput for user input
        self.input_text = TextInput(hint_text='Enter website example "google.com"', multiline=False)
        layoutTop.add_widget(self.input_text)

        # Create a Button and bind the function to it
        btn = Button(text='Scan website', on_press=self.scan)
        layoutTop.add_widget(btn)

        layout.add_widget(layoutTop)

        layoutAttackBar = BoxLayout(orientation='horizontal', spacing=10, padding=10)

        attackType = BoxLayout(orientation='vertical', spacing=10, padding=10)
        #label
        #button to change label

        layoutAttack = BoxLayout(orientation='vertical', spacing=10, padding=10)
        attack = Label(text='Keywords to check')
        layoutAttack.add_widget(attack)

        self.attack_list = TextInput(text="checklist.txt", hint_text='Enter file to save results to', multiline=False)
        layoutAttack.add_widget(self.attack_list)
        layoutAttackBar.add_widget(layoutAttack)

        layoutWhere = BoxLayout(orientation='vertical', spacing=10, padding=10)
        where = Label(text='Result will load her')
        layoutWhere.add_widget(where)

        self.output_where = TextInput(text="results.txt", hint_text='Enter file to save results to', multiline=False)
        layoutWhere.add_widget(self.output_where)

        layoutAttackBar.add_widget(layoutWhere)

        layout.add_widget(layoutAttackBar)

        # Result added here
        #self.result_label = Label(text='Result will load here', size_hint_x=None, size_hint_y=None)
        #layout.add_widget(self.result_label)

        layoutType = BoxLayout(orientation='horizontal', spacing=10, padding=10)

        # Create the main button
        self.main_button = Button(text="Select an engine type", size_hint=(None, None), size=(520, 70))

        self.engineDropDown = DropDown()
        for engineType in ["gobuster_Windows_i386", "gobuster_Windows_x86_64", "gobuster_Windows_arm64", "gobuster_Linux_i386", "gobuster_Linux_arm64", "gobuster_Darwin_x86_64", "gobuster_Darwin_arm64"]:
        
            # Adding button in drop down list
            btn = Button(text=engineType, size_hint_y=None, height=70)
        
            # binding the button to show the text when selected
            btn.bind(on_release=lambda btn: self.on_select_option(btn.text, self.engineDropDown, self.main_button))
        
            # then add the button inside the dropdown
            self.engineDropDown.add_widget(btn)

        # Attach the dropdown to the main button
        self.main_button.bind(on_release=self.engineDropDown.open)

        self.type_button = Button(text="Scan type", size_hint=(None, None), size=(520, 70))

        self.scanType = DropDown()
        for engineType in ["dir", "dns"]:
        
            # Adding button in drop down list
            btn = Button(text=engineType, size_hint_y=None, height=70)
        
            # binding the button to show the text when selected
            btn.bind(on_release=lambda btn: self.on_select_option(btn.text, self.scanType, self.type_button))
        
            # then add the button inside the dropdown
            self.scanType.add_widget(btn)

        # Attach the dropdown to the main button
        self.type_button.bind(on_release=self.scanType.open)

        layoutType.add_widget(self.main_button)
        layoutType.add_widget(self.type_button)

        layout.add_widget(layoutType)

        return layout

    def scan(self, instance):
        #self.input_text.text
        #self.result_label.text = 
        run_command_line_tool(website=self.input_text.text, hitList=self.attack_list.text, results=self.output_where.text, type=self.type_button.text, engine=self.main_button.text)

    def on_select_option(self, text, dropdown, that_button):
        # Update the main button text with the selected option
        that_button.text = f"{text}"
        # Close the dropdown
        dropdown.dismiss()
        
if __name__ == '__main__':
    MyApp().run()

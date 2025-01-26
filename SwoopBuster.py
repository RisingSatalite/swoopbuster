from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
import subprocess

def run_command_line_tool(website, hitList="checklist.txt", results="results.txt", goBusterType="gobuster_Windows_i386", type="dir"):
    try:
        # Construct the command
        # scan = "ls"
        #scan = f"./gobuster dir -u https://{website} -w ../../{hitList} -o ../../{results}"
        #command = f"cd gobuster/{goBusterType} && {scan}"

        command = f"./gobuster/{goBusterType}/gobuster {type} -u https://{website} -w {hitList} -o {results}"
        #command = f"cd gobuster && cd {goBusterType} && {scan}"
        #command = [f"cd gobuster/{goBusterType} && ls -l"]
        #command = [f"cd gobuster/{goBusterType} && ./gobuster"]

        # Split the command into a list of arguments
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
    #except FileNotFoundError:
        #print("Error: The gobuster command was not found.")
        #return None
    except Exception as e:
        print("An error occurred:", str(e))
        return None

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
        self.result_label = Label(text='Result will load her')
        layout.add_widget(self.result_label)

        return layout

    def scan(self, instance):
        self.result_label.text = run_command_line_tool(website=self.input_text.text, hitList=self.attack_list.text, results=self.output_where.text)
        
if __name__ == '__main__':
    MyApp().run()

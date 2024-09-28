import os
import sys
import shodan
import requests
import gradio as grad

# Define the file path for the `bella.chr` file.
def get_chr_file_path():
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), "bella.chr")

# Check for the existence of the `bella.chr` file and proceed accordingly.
def connect_to_bella():
    file_path = get_chr_file_path()
    if os.path.isfile(file_path):
        print("file found")
        connect_bot()
    else:
        print("bella.chr file not found. Please provide the correct path.")
        # Ask user for the new path if not found.
        custom_path = input("Enter the path to bella.chr: ")
        if os.path.isfile(custom_path):
            print("File found at the provided path. Connecting to the bot...")
            connect_bot()
        else:
            print("File not found at the provided path. Exiting.")
            sys.exit()

# Connect to the bot and start the program.
def connect_bot():
    switch = input("Would you like to boot up bella.ai? (Yes/No): ").strip().lower()
    if switch == "yes":
        print("Connecting to the bot...")
        # Connection logic here (placeholder)
        success = True  # Simulate successful connection for demonstration.
        if success:
            computer_name = os.getenv("COMPUTERNAME", "User")
            print(f"Hello, {computer_name}. Bella AI is now online.")
            # Proceed with the program
        else:
            print("Connection failed. Please try again.")
            sys.exit()
    else:
        print("Exiting the program.")
        sys.exit()

# Handle Shodan interaction
def interact_with_shodan():
    shodan_switch = input("Would you like to interact with Shodan? (Yes/No): ").strip().lower()
    if shodan_switch == "yes":
        api_key = input("Enter your Shodan API key: ").strip()
        api = shodan.Shodan(api_key)

        search_query = input("Enter the search keyword: ")
        try:
            results = api.search(search_query)
            print(f"Shodan found {results['total']} results for '{search_query}'")
            for result in results['matches']:
                print(f"IP: {result['ip_str']} - {result['data']}")
        except shodan.APIError as e:
            print(f"Error: {e}")

# Make a gradio GUI app for a random anime girl image
def display_anime_girl():
    def generate_image():
        # Replace this URL with an actual API if available
        url = "https://thispersondoesnotexist.com/image"
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            return "Failed to fetch image."

    gradio_interface = grad.Interface(fn=generate_image, inputs=None, outputs="image", title="Anime Girl Generator")
    gradio_interface.launch()

# Main function to run the program.
if __name__ == "__main__":
    connect_to_bella()
    print("Welcome to bella.ai")
    netcat_switch = input("Would you like to netcat and scan the local computers? (Yes/No): ").strip().lower()
    if netcat_switch == "yes":
        # Placeholder for netcat functionality
        print("Netcat scanning is currently in beta...")

    interact_with_shodan()

    anime_switch = input("Would you like to display a random anime girl image? (Yes/No): ").strip().lower()
    if anime_switch == "yes":
        display_anime_girl()

    print("Thank you for using Bella's CPanel v0.2 by @Bella_AI")

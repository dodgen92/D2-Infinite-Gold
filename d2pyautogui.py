import pyautogui
import pygetwindow as gw
import time
import keyboard

# Delay between each action (in seconds)
delay_between_actions = 1

# Get the target window
target_window_title = "Diablo II: Resurrected"
target_window = gw.getWindowsWithTitle(target_window_title)[0]

# Positions 
sellBTN_position = (725, 888)
sellItem_position = (1031, 320)
buyItemback_position = (770, 322)

try:
    # Activate the target window
    target_window.activate()

    while True:
        # Left click to sell
        pyautogui.click(target_window.left + sellBTN_position[0], target_window.top + sellBTN_position[1])
        print("Clicking sell button", sellBTN_position)
        time.sleep(delay_between_actions)

        # Double click to sell item
        pyautogui.click(target_window.left + sellItem_position[0], target_window.top + sellItem_position[1])
        print("Selling item", sellItem_position)
        time.sleep(delay_between_actions)

        # Double click again to confirm selling item
        pyautogui.click(target_window.left + sellItem_position[0], target_window.top + sellItem_position[1])
        print("Confirming selling item", sellItem_position)
        time.sleep(delay_between_actions)

        # Right click to buy back item
        pyautogui.rightClick(target_window.left + buyItemback_position[0], target_window.top + buyItemback_position[1])
        print("Buying item back", buyItemback_position)
        time.sleep(delay_between_actions)

        # Check if 'q' key is pressed to quit the script
        if keyboard.is_pressed('q'):
            print("Script terminated by user.")
            break

except Exception as e:
    print("An error occurred:", e)

print("Script finished.")
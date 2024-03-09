Slice of Life Ordering System Manual

Welcome to the Pizza Ordering System! This system allows you to select different types and sizes of pizzas and view your selections before proceeding to checkout.

1. Main Window:
When you run the program, the main window opens up. In this window, you'll see six groups, each representing a type of pizza. Each group contains four bubbles representing different sizes of pizzas. To make a selection:

•	Click on the bubble corresponding to the desired pizza size in each group.
•	You can only select one size per pizza type.
•	Once selected, the bubble will turn blue to indicate your choice.

Your current selections are listed under each pizza type in the selection box on the right side of the window.
At the bottom of the selection box, the total price of your current selections will be displayed.

2. Checkout:
To proceed to checkout, click the "Open Checkout" button at the bottom of the selection box. This will open a new window.

You'll see a message in the checkout window thanking you for your purchase. Your selections and total price will not be shown here; this window is simply for confirmation.

3. Exiting the Program:
To exit the program, close the main or checkout window.

That's it! Enjoy ordering your pizzas with the Pizza Ordering System!

-----------------------------------------------------------------------------------------------------------------------------------

Validations/Hurdles
Background Image
I encountered several issues while coding this GUI. Initially, Tkinter failed to recognize the file path required to use the image. The image still couldn't be accessed despite going through the troubleshooting process of verifying file integrity, ensuring the file patch was correct, and uninstalling and reinstalling associated files. It turned out that the image file could not be accessed due to the administration's permissions and the file's location, which was trying to be called. The file struggled to access the image since it was on a separate driver. I resolved this issue by tweaking the priority of the GUI to set the boxes that display the information to prioritize the visual load order so they can be displayed over the canvas (image background).

Getting the image to cooperate was perhaps the biggest hurdle I had, despite it being what would have seemed like one of the more straightforward solutions, as it often disappeared randomly. I eventually got it working consistently by setting its position to be called low in the main but higher than the references that call it out in the other classes.

Second Window Button
The second window button was another issue that I struggled with. Although I eventually found a solution, which was to extend the window to just enough space for the second window button to be visible beneath the image I inputted, I was unable to figure out how to place the checkout button beneath the prices as I had originally intended.

Selection Box
Getting the Selection box to update its behavior with clicking buttons was more hassle than I thought. There was much going back and forth with the code and trying to stay on task with what I had envisioned versus the natural complexities of implementing that code. I underestimated how difficult it would be to have functioning buttons that did what you wanted (4 options; the buttons could be unselected and tied to the selection window) while also having to stay in front of the canvas. I eventually got it working by setting variables between the class BubbleBox and SelectionWindow, so they played nicely together.

Second Window
Initially, the second window was going to be the checkout window. However, I wasn't able to figure out how to grab the calculations that were used in the first window and make them cooperate with the second window. I made too many variables work in niche ways, causing the code to become a bigger mess than I had initially planned to function correctly with the second window. So, it was just a "thank you" window instead.

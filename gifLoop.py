from PIL import Image, ImageSequence

def make_gif_loop(filename):
    # Open the GIF file
    with Image.open(filename) as img:
        # Ensure the image is a gif
        if img.format == 'GIF':
            # Convert to a list of frames as some GIFs can be optimized
            frames = [frame.copy() for frame in ImageSequence.Iterator(img)]
            
            # Set the duration for each frame if needed, or keep the original
            frames = [frame.copy() for frame in frames]
            
            # Save the frames as a new looping GIF
            frames[0].save('looping_output.gif', save_all=True, append_images=frames[1:], loop=0)
            print("GIF is now set to loop continuously and saved as 'looping_output.gif'")
        else:
            print("The provided file is not a GIF.")

# Use the function with the file 'output.gif'
make_gif_loop('output.gif')

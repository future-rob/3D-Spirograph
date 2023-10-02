 # Spirograph Blender Code V1.1

Spirograph Blender Code is a Python script designed for use in Blender; to visualize complex datasets through the unique creation of 3D multi-axis spirographs.

## Features

1. **Create 3D Spirograph**: Encode complex parameters including radius, loops, and coordinates into a visually appealing 3D spirograph.

2. **Decode Existing Spirograph**: Reverse-engineer an existing spirograph to decode the unique parameters that were used in its creation.

3. **Unique Identification of Spirographs**: Generate a unique hash identifier for each spirograph based on the input parameters.

4. **Scalability**: Control the granularity and complexity of your spirograph by adjusting the number of samples within the script.

## How to Use

1. **Install Dependencies**: Make sure you have `numpy`, `bpy`, `hashlib`, and `scipy` installed in your environment.

2. **Run the Script**: Open Blender and run the script in it. For creating a spherical spiral, call the function `create_spherical_spiral()`. Pass the parameters of radius, loops and coordinates. The function will return the created spirograph object and the points forming the spiral.

3. **Decode a Spherical Spiral**: To decode an existing spirograph, call the function `decode_spherical_spiral()`. Pass the points of the spiral and the parameter space. The function will return the parameters that result in the minimal total distance.

## Use-cases 

1. **Data Visualization**: The script is ideal for creating complex data visualizations, making it easier to understand and interpret data. 

2. **Design and Art**: Artists and designers can use this tool to create unique pieces of art or design elements.

3. **Scientific Simulation**: This function can be used to simulate real-world natural phenomena such as galaxies or weather patterns.

Please note that this script is intended for use in the Blender environment. You will need to have Blender installed on your system to use it.
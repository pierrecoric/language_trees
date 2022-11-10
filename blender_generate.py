#bpy.ops.mesh.primitive_cube_add(enter_editmode=False, align='WORLD', location=(x, y, z), scale=(x, y, z))



letterFrequencies = [[9, 11, 2, 21, 16, 2, 5, 14, 6, 1, 4, 1, 6, 1, 8, 2, 0, 3, 8, 18, 0, 23, 5, 0, 0, 14], [31, 0, 5, 0, 68, 1, 0, 0, 15, 0, 0, 2, 5, 13, 17, 2, 0, 6, 2, 2, 9, 1, 1, 0, 0, 0], [12, 4, 5, 3, 10, 0, 5, 3, 1, 4, 5, 10, 4, 34, 6, 2, 0, 11, 4, 15, 2, 1, 1, 0, 1, 0], [8, 0, 0, 9, 25, 1, 2, 7, 3, 0, 5, 1, 2, 10, 9, 0, 0, 13, 7, 4, 1, 0, 1, 0, 0, 3], [4, 1, 4, 0, 22, 0, 4, 0, 6, 0, 1, 12, 0, 10, 3, 1, 0, 6, 4, 9, 0, 1, 0, 0, 0, 0], [3, 0, 2, 1, 11, 0, 2, 4, 6, 0, 2, 6, 0, 10, 3, 0, 0, 6, 1, 14, 1, 0, 0, 0, 0, 1], [0, 6, 0, 0, 9, 1, 0, 4, 8, 0, 0, 1, 0, 11, 3, 0, 0, 3, 3, 6, 0, 2, 0, 0, 0, 0], [4, 0, 1, 1, 17, 0, 2, 1, 1, 0, 2, 1, 0, 5, 0, 2, 0, 2, 1, 3, 1, 0, 0, 0, 0, 0], [1, 0, 0, 1, 10, 0, 3, 1, 2, 0, 5, 2, 0, 1, 0, 0, 0, 3, 1, 2, 0, 0, 0, 0, 0, 0], [2, 0, 0, 3, 1, 0, 0, 0, 2, 0, 6, 2, 0, 1, 0, 0, 0, 2, 2, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 2, 6, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 5, 1, 0, 0, 1, 0, 0, 0, 0], [0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]




for i in range(len(letterFrequencies)):
    for n in range(len(letterFrequencies[i])):
        if(letterFrequencies[i][n] > 0):
            #bpy.ops.mesh.primitive_cube_add(enter_editmode=False, align='WORLD', location=(i*5, n/2, letterFrequencies[i][n] / 4), scale=(0.1, 0.1, letterFrequencies[i][n] / 4))
            bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, enter_editmode=False, align='WORLD', location=(i/2, n/2, letterFrequencies[i][n] / 6), scale=(0.1, 0.1, letterFrequencies[i][n] / 6))

import glfw
from OpenGL import GL
import numpy as np


def process_inputs(window):
    if glfw.get_key(window, glfw.KEY_ESCAPE) == glfw.PRESS:
        glfw.set_window_should_close(window, True)


def main():

    # set up the window
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL.GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    glfw.window_hint(glfw.RESIZABLE, False)

    window = glfw.create_window(640, 480, "Success", None, None)
    glfw.make_context_current(window)

    vertex_shader_source = '''#version 330 core
    layout (location = 0) in vec3 aPos;

    void main()
    {
        gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);
    }'''

    vertex_shader = GL.glCreateShader(GL.GL_VERTEX_SHADER)
    GL.glShaderSource(vertex_shader, vertex_shader_source)
    GL.glCompileShader(vertex_shader)

    frag_shader_source = '''#version 330 core
    out vec4 frag_color;

    void main()
    {
        frag_color = vec4(1.0f, 0.5f, 0.2f, 1.0f);
    }'''

    frag_shader = GL.glCreateShader(GL.GL_FRAGMENT_SHADER)
    GL.glShaderSource(frag_shader, frag_shader_source)
    GL.glCompileShader(frag_shader)

    shader_program = GL.glCreateProgram()
    GL.glAttachShader(shader_program, vertex_shader)
    GL.glAttachShader(shader_program, frag_shader)
    GL.glLinkProgram(shader_program)
    GL.glDeleteShader(vertex_shader)
    GL.glDeleteShader(frag_shader)

    # clear the color
    GL.glClearColor(0.2, 0.3, 0.3, 1.0)

    # declare the vertex positions in the interval [-1, 1]
    # vertices = np.array([
    #     [0, 0.5, 0],
    #     [0.5, -.5, 0],
    #     [-.5, -.5, 0],
    # ], 'f')

    vertices = np.array([
        [0.5, 0.5, 0.0],  # top right
        [0.5, -0.5, 0.0],  # bottom right
        [-0.5, -0.5, 0.0],  # bottom left
        [-0.5, 0.5, 0.0],  # top left
    ], 'f')

    indices = np.array((0, 1, 3, 1, 2, 3), np.uint32)

    # create a vertex array
    vertex_array = GL.glGenVertexArrays(1)
    GL.glBindVertexArray(vertex_array)

    buffers = GL.glGenBuffers(2)
    GL.glBindBuffer(GL.GL_ARRAY_BUFFER, buffers[0])
    GL.glBufferData(GL.GL_ARRAY_BUFFER, vertices, GL.GL_STATIC_DRAW)

    GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER, buffers[1])
    GL.glBufferData(GL.GL_ELEMENT_ARRAY_BUFFER, indices, GL.GL_STATIC_DRAW)

    GL.glVertexAttribPointer(0, 3, GL.GL_FLOAT, GL.GL_FALSE, 0, None)
    GL.glEnableVertexAttribArray(0)

    while not glfw.window_should_close(window):
        process_inputs(window)

        GL.glClearColor(0.2, 0.3, 0.3, 1.0)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)

        GL.glUseProgram(shader_program)
        GL.glBindVertexArray(vertex_array)
        # GL.glDrawArrays(GL.GL_TRIANGLES, 0, 3)
        GL.glDrawElements(GL.GL_TRIANGLES, 6, GL.GL_UNSIGNED_INT, None)

        glfw.swap_buffers(window)
        glfw.poll_events()


if __name__ == '__main__':
    glfw.init()
    main()
    glfw.terminate()

#version 330 core

// global color variable
uniform vec3 global_color;

// receiving interpolated color for fragment shader
flat in vec3 fragment_color;

// output fragment color for OpenGL
out vec4 out_color;

void main() {
    out_color = vec4(fragment_color + global_color, 1);
}
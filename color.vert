#version 330 core

layout(location = 0) in vec3 position;
layout(location = 1) in vec3 color;

out vec4 clip;

void main() {
    gl_Position = vec4(position, 1);
    clip = vec4(color, 1);
}

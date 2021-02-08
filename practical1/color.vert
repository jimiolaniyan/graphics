#version 330 core

layout(location = 0) in vec3 position;
layout(location = 1) in vec3 color;

uniform mat4 matrix;

out vec4 clip;

void main() {
    gl_Position = matrix * vec4(position, 1);
    clip = vec4(color, 1);
}

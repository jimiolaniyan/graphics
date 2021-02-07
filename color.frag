#version 330 core

uniform vec3 color;
out vec4 outColor;
in vec4 clip;

void main() {
    outColor = vec4(color, 1) + clip;
}

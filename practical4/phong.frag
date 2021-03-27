#version 330 core

// fragment position and normal of the fragment, in WORLD coordinates
// (you can also compute in VIEW coordinates, your choice! rename variables)
in vec3 w_position, w_normal;   // in world coodinates

// light dir, in world coordinates
uniform vec3 light_dir;

// material properties
uniform vec3 k_d;

// ambient properties
uniform vec3 k_a;

// specular properties
uniform vec3 k_s;

uniform float s;

// world camera position
uniform vec3 w_camera_position;

out vec4 out_color;

void main() {
    // TODO: compute Lambert illumination
    vec3 n = normalize(w_normal);
//    out_color = vec4(k_d * max(0, dot(n, -light_dir)), 1);
    vec3 r = normalize(reflect(light_dir, n));
    vec3 v = normalize(w_camera_position - w_position);
    out_color = vec4((k_a + (k_d * max(0, dot(n, -light_dir))) + (k_s * pow(dot(r, v), s))), 1);
}
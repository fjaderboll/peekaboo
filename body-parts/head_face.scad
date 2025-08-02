use <head_tilt.scad>
use <addon_support.scad>

margin = 0.20;
offset_x = -(34.4 + 3.8*2)/2;
offset_y = 5;
offset_z = 25 + 2*5 + 3.8 + margin;

skull_scale_z = 0.6;

module head_face_skull() {
    color("blue")
    difference() {
        difference() {
            translate([0, 21, offset_z+5])
            scale([1, 1, skull_scale_z])
            rotate(90, [1, 0, 0])
            cylinder(h=30, r=32, $fn=8);
            
            translate([0, 22, offset_z+5])
            scale([1, 1, skull_scale_z])
            rotate(90, [1, 0, 0])
            cylinder(h=40, r=30, $fn=8);
        }
        
        translate([-30, -5, 18.5])
        cube([60, 30, 20]);
    }
}

module head_face_face() {
    // face
    color("white")
    difference() {
        translate([0, -5, offset_z+5])
        scale([1, 1, skull_scale_z])
        rotate(90, [1, 0, 0])
        cylinder(h=2, r=30, $fn=8);
        
        // left eye
        translate([10.5, -4.9, offset_z+5])
        rotate(90, [1, 0, 0])
        cylinder(h=3, r=7, $fn=4);
        
        // right eye
        translate([-14.5, -4.9, offset_z+5])
        rotate(90, [1, 0, 0])
        cylinder(h=3, r=7, $fn=8);
    }
}

module head_face_mount_main(side) {
    translate([offset_x*side, offset_y, offset_z])
    rotate(90*side, [0, 0, 1])
    addon_bar(12, single_clip=true);
}

module head_face_mount_antenna(side) {
    translate([(offset_x-4.0)*side, offset_y, offset_z+15])
    rotate(35*side, [0, 1, 0])
    rotate(90*side, [0, 0, 1])
    addon_holder();
}

module head_face() {
    head_face_skull();
    head_face_face();
    
    head_face_mount_main(-1);
    head_face_mount_main(1);
    
    head_face_mount_antenna(-1);
    head_face_mount_antenna(1);
}

% color("gray") head_tilt();
head_face();

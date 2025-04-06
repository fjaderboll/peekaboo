use <head_base.scad>

frame_width = 15;
frame_height = 25;
frame_thickness = 3.8;
frame_inner_length = 31.6+frame_thickness-1.0;

axel_diameter = 7;
axel_offset_y = 5;
axel_offset_z = 5;

margin = 0.20;

module head_tilt_frame_arm() {
    hull() {
        translate([0, -frame_width/2, 0])
        cube([frame_thickness, frame_width, frame_thickness]);
        
        translate([0, 0, -frame_height])
        rotate(90, [0, 1, 0])
        cylinder(h=frame_thickness, d=11);
    }
}

module head_tilt_frame_arm_left() {
    difference() {
        color("yellow") head_tilt_frame_arm();
        
        color("red")
        translate([-frame_thickness/2, 0, -frame_height])
        rotate(90, [0, 1, 0])
        cylinder(h=frame_thickness*2, d=axel_diameter+margin*2, $fn=80);
    }
}

module head_tilt_frame_arm_right() {
    difference() {
        color("yellow") head_tilt_frame_arm();
        
        color("red") translate([-frame_thickness+1.65, 0, -frame_height])
        rotate(90, [1, 0, 0])
        rotate(90, [0, 1, 0])
        mount_single();
    }
}

module head_tilt_frame() {
    difference() {
        color("orange")
        translate([-frame_inner_length/2, -frame_width/2, 0])
        cube([frame_inner_length, frame_width, frame_thickness]);
        
        color("red")
        translate([0, 0, -frame_thickness/2])
        scale([1, 0.3, 1])
        cylinder(h=frame_thickness*2, r=frame_inner_length/2*0.7);
    }
    translate([-frame_inner_length/2-frame_thickness, 0, 0])
    head_tilt_frame_arm_left();
    
    translate([frame_inner_length/2, 0, 0])
    head_tilt_frame_arm_right();
}

module head_tilt() {
    % head_base();
    
    translate([0, 0, axel_offset_z*2])
    translate([0, axel_offset_y, 0])
    rotate(0, [1, 0, 0])
    translate([0, 0, frame_height])
    head_tilt_frame();
}

head_tilt();

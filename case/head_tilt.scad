use <head_base.scad>

frame_inner_length = 31.1;
frame_width = 10;
frame_height = 21;
frame_thickness = 3.8;

axel_diameter = 7;

margin = 0.20;

module head_tilt_frame_arm() {
    hull() {
        translate([0, -frame_width/2, 0])
        cube([frame_thickness, frame_width, frame_thickness]);
        
        translate([0, 0, -frame_height])
        rotate(90, [0, 1, 0])
        cylinder(h=frame_thickness, d=10);
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
    color("orange")
    translate([-frame_inner_length/2, -frame_width/2, 0])
    cube([frame_inner_length, frame_width, frame_thickness]);
    
    translate([-frame_inner_length/2-frame_thickness, 0, 0])
    head_tilt_frame_arm_left();
    
    translate([frame_inner_length/2, 0, 0])
    head_tilt_frame_arm_right();
}

module head_tilt() {
    % color("pink") head_base();
    
    translate([0, 0, 5.5*2])
    rotate(00, [1, 0, 0])
    translate([0, 0, frame_height])
    head_tilt_frame();
}

head_tilt();

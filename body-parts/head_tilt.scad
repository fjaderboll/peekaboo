use <head_base.scad>
use <mount_heat_camera.scad>
use <mount_pir.scad>
use <addon_support.scad>

frame_width = 14;
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
        cylinder(h=frame_thickness, d=14);
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
        
        /*color("red")
        translate([0, 0, -frame_thickness/2])
        scale([0.25, 0.25, 1])
        cylinder(h=frame_thickness*2, r=frame_inner_length/2);*/
    }
    translate([-frame_inner_length/2-frame_thickness, 0, 0])
    head_tilt_frame_arm_left();
    
    translate([frame_inner_length/2, 0, 0])
    head_tilt_frame_arm_right();
}

module head_tilt() {
    // frame
    translate([0, 0, axel_offset_z*2])
    translate([0, axel_offset_y, 0])
    rotate(0, [1, 0, 0])
    translate([0, 0, frame_height])
    head_tilt_frame();
    
    // mounts
    mount_offset_y = axel_offset_y - frame_width/2;
    mount_offset_z = frame_height + axel_offset_z*2;
    
    translate([10.3, mount_offset_y+4.7, mount_offset_z+frame_thickness-1.4])
    rotate(-90, [0, 0, 1])
    mount_heat_camera();
    
    translate([-14.4, mount_offset_y, mount_offset_z+frame_thickness-1.4])
    rotate(-90, [0, 0, 1])
    mount_pir();
    
    // addon holders
    translate([-(frame_inner_length+2*frame_thickness)/2, mount_offset_y+frame_width/2, mount_offset_z+frame_thickness])
    rotate(90, [0, 0, 1])
    addon_holder();
    
    translate([(frame_inner_length+2*frame_thickness)/2, mount_offset_y+frame_width/2, mount_offset_z+frame_thickness])
    rotate(-90, [0, 0, 1])
    addon_holder();
}

% color("gray") head_base();
head_tilt();

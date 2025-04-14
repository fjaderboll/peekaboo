use <addon_servo.scad>

mount_diameter1 = 7;
mount_diameter2 = 6;
mount_diameter3 = 4.5;
mount_quad_diameter = 3.7;
mount_quad_length = 20;
mount_height = 1.5;
mount_length = 15.5;
margin = 0.20;

servo_width = 16.4;
servo_height = 12.5;

base_diameter = 40;
base_width = servo_height + 5.5 * 2 + 0.5;
base_height = 3.8;

axel_diameter = 7;
axel_offset_y = 5;
axel_offset_z = 5;

module head_base_plate() {
    color("pink") difference() {
        cylinder(h=base_height, d=base_diameter, $fn=16);
    
        translate([base_width/2, -base_diameter/2, -1]) cube([base_diameter/2, base_diameter, base_height+2]);
        translate([-base_width/2-base_diameter/2, -base_diameter/2, -1]) cube([base_diameter/2, base_diameter, base_height+2]);
    }
}

module mount_center() {
    color("red")
    translate([0, 0, -mount_height-margin])
    cylinder(h=base_height+2, d=mount_diameter1+2*margin, $fn=40);
}

module mount_single() {
    mount_center();
    
    color("red")
    translate([0, 0, base_height-mount_height-margin])
    hull() {
        cylinder(h=mount_height+margin*2, d=mount_diameter2+margin, $fn=40);
        
        translate([0, mount_length-mount_diameter3/2+margin, 0])
        cylinder(h=mount_height+margin*2, d=mount_diameter3+margin, $fn=40);
    }
}

module mount_double() {
    mount_single();
    rotate(180, [0, 0, 1]) mount_single();
}

module mount_quad_double() {
    mount_center();
    
    color("red")
    translate([0, 0, base_height-mount_height-margin])
    hull() {
        translate([0, -mount_quad_length/2+mount_quad_diameter/2-margin, 0])
        cylinder(h=mount_height+margin*2, d=mount_quad_diameter+margin, $fn=20);
        
        translate([0, mount_quad_length/2-mount_quad_diameter/2+margin, 0])
        cylinder(h=mount_height+margin*2, d=mount_quad_diameter+margin, $fn=20);
    }
}

module mount_quad() {
    rotate(45, [0, 0, 1]) mount_quad_double();
    rotate(135, [0, 0, 1]) mount_quad_double();
}

module servo_holder_fixed() {
    difference() {
        translate([servo_height/2, 0, servo_width/2+base_height-2]) rotate(90, [0, 1, 0]) servo_holder();
        translate([0, 0, 0.001]) head_base_plate();
        
        color("red")
        translate([0, 0, -servo_width/2])
        cylinder(h=servo_width*2, d=mount_diameter1+2*margin, $fn=20);
    }
}

module tilt_point() {
    color("orange")
    translate([-base_width/2, 0, 0])
    rotate(-90, [0, 1, 0])
    union() {
        hull() {
            translate([0, -10, 0])
            cube([base_height, 20.57, base_height]);
            
            translate([axel_offset_z*2, 0, 0])
            cylinder(h=base_height, d=10, $fn=20);
        }
        // axel
        translate([axel_offset_z*2, 0, base_height])
        cylinder(h=base_height+0.5, d=axel_diameter, $fn=80);
    }
}

module head_base() {
    difference() {
        head_base_plate();
        mount_quad();
    }
    servo_holder_fixed();
    
    translate([0, axel_offset_y, 0])
    tilt_point();
}

head_base();


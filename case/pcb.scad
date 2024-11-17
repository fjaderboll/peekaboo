pt = 1.5;  // PCB thickness

module pcb(width, height) {
    d = 3.5;
    $fn = 10;
    
    difference() {
        union() {
            color("green") translate([0, 0, -pt/2]) cube([width, height, pt]);
            
            color("#ccc") {
                for(x = [5 : d : width-3]) {
                    for(y = [5 : d : height-3]) {
                        translate([x, y, 0]) cylinder(h=pt*1.2, d=2, center=true);
                    }
                }
            }
        }
        color("#ccc") {
            for(x = [5 : d : width-3]) {
                for(y = [5 : d : height-3]) {
                    translate([x, y, 0]) cylinder(h=pt*1.4, d=1, center=true);
                }
            }
        }
    }
}

pcb(64.4, 53.5);
translate([64.4+2.6, 0, 0]) pcb(20, 80);

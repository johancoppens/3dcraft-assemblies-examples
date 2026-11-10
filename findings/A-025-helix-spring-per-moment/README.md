# Performance: a helical spring that follows `t` is very expensive per moment

Found while building `task-lamp` at 3DCraft 150f0015.

```sh
craft3d-cli run --new '{"units":"mm"}' --script helix_spring.json --out helix_spring.3dcraft
craft3d-cli run --new '{"units":"mm"}' --script repro.json
```

A 30-coil spring is a `datum.helix` and one `feature.sweep` (document tolerance 1e-3 mm, already eased from the default
1e-6). A part regeneration takes 1.1 s (load average 14 to 26, a laptop with 14 cores), and the spring's `span` follows
`t`: `motion.bake` at 120 frames took 43 s, and 75 s on a second run at load 40 (it builds 213 to 214 configurations of the
spring: 200 to 350 ms each).

**Should:** a coil spring is the first thing an assembly wants to rebuild per moment, and `feature.sweep` along a helix
is the natural way to write it; it builds about 120 B-spline faces per configuration. A cheap route for an exact
helical sweep, or a rigid-pitch instanced coil (one turn repeated along its axis, as `feature.pattern` does) that
needs no boolean of touching turns. **Impact:** the helical sweep cannot be used for a spring that follows `t` at this
tier; `task-lamp` draws its coils as half-turn `feature.revolve`s and two `feature.pattern`s, 23 ms per configuration on
the same machine (at load 39) and a coil that matches the helix sweep in the picture, with real wire and coil count.

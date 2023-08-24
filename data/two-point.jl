module Shit
import CorrelationFunctions.Utilities as U
import CorrelationFunctions.Directional as D
using Statistics
using NPZ

function do_it!()
    data = U.read_cuboid("test.raw", 300, 3)
    for sym in [:s2, :c2]
        fn = D.eval(sym)
        cf = fn(data, false; periodic = true) |> mean
        npzwrite("test-$(sym).npy", cf)
    end
end

end

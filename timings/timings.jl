module Shit
import CorrelationFunctions.Directional as D
using NPZ

const functions = [
    :s3, :c3, :surf3, :surf2void, :surfvoid2
]

function counttime(thunk)
    t = time()
    thunk()
    return time() - t
end

function do_it()
    x = 125000:2500000:27000000
    sides = round.(Int, cbrt.(x))
    for sym in functions
        println(sym)
        fn = D.eval(sym)
        times = map(sides) do side
            println(side)
            GC.gc()
            data = rand(Bool, (side, side, side))
            counttime(() -> fn(data, true; periodic = true))
        end
        npzwrite("$(sym).npy", hcat(sides, times))
    end
    return nothing
end

end

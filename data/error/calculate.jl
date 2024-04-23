module Shit
import CorrelationFunctions.Directional as D
import CorrelationFunctions.Utilities as U
using NPZ
using CUDA

const fns = [D.surf3, D.s3]

function foo(path)
    for fn in fns
        for s in 1:9
            println(s)
            data = joinpath(path, "data-$(s)-300.npy") |> npzread |> CuArray
            cf = fn(data; periodic = true)[D.PlaneXY()]
            npzwrite(joinpath(path, "data-$(s)-300-$(fn).npy"), cf)
        end
    end
end

end

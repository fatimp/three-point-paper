module Shit
import CorrelationFunctions.Directional as D
import CorrelationFunctions.Utilities as U
using NPZ
using CUDA

const fns = [D.surf3, D.s3]

function foo(path)
    for fn in fns
        for s in 1:9
            for side in [300, 600]
                println(side)
                data = joinpath(path, "data-$(s)-$(side).npy") |> npzread |> CuArray
                cf = fn(data; periodic = true)[D.PlaneXY()]
                npzwrite(joinpath(path, "data-$(s)-$(side)-$(fn).npy"), cf)
            end
        end
    end
end

end

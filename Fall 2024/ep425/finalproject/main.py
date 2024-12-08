import matplotlib.pyplot as plt
import pandas as pd
import utils.tools as tl


# %% read data table
table1 = "data/Observed data/20241123/HD 21447 (comparison star)/pipelineout/Table-HD21447-g15s-20241123.tbl"
test1 = tl.read_table(table1)
test1 = tl.calc_instrumental_magnitude(test1)

fig2, axes2 = plt.subplots(2, 1, figsize=(10, 7), tight_layout=True, sharex=True)
axes2[0].plot(test1["BJD_TDB"], test1["SourceSky2"])
axes2[1].plot(test1["BJD_TDB"], test1["AIRMASS"])

axes2[0].set_ylabel("Instrumental Magnitudes")
axes2[1].set_ylabel("Airmass")
axes2[0].set_xlabel("Time (BJD_TBD)")
axes2[1].set_xlabel("Time (BJD_TBD)")

axes2[0].set_title("Light Curve Pot - 11/23/2024")
axes2[1].set_title("Airmass vs. Time")
fig2.suptitle("HD 237190 (cepheid) - Light Curve & Airmass")
fig2.savefig(r"figures/HD_237190_cepheid_Light_Curve_Airmass.jpg")

# %% read data table
table2 = "data/Observed data/20241116/HD 237190/HD237190-g30s-table.tbl"
test2 = tl.read_table(table2)

fig3, axes3 = plt.subplots(figsize=(10, 7), tight_layout=True)
axes3.plot(test2["JD_UTC"], test2["rel_flux_T1"])
axes3.set_ylabel("Instrumental Magnitudes")
axes3.set_xlabel("Time (BJD_TBD)")
fig3.suptitle("HD 237190 Light Curve (cepheid) - Green Filter. Taken 11/16/2024", size=15)
fig3.savefig(r"figures/HD_237190_Light_Curve_cepheid_Green_Filter_Taken_11_16_2024.jpg")
plt.show()


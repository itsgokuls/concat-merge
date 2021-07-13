import pandas as pandas_data_frame

# Read Files into dataframe values
file1 = pandas_data_frame.read_excel("Book1.xlsx")
file2 = pandas_data_frame.read_excel("Book2.xlsx")

# Filter applied to find non-NaN values
with_cve_file1 = file1.dropna()
with_cve_file2 = file2.dropna()

# Filter applied to find NaN values
without_cve_file1 = file1[file1["CVE"].isnull()]
without_cve_file2 = file2[file2["CVE"].isnull()]

# Merged Both files on column CVE with filtered values(non - NaN)
merged_cve_values = pandas_data_frame.merge(with_cve_file1, with_cve_file2, on='CVE', how='inners')

# Merged Both files with filtered values(NaN)
merged_non_cve_values = pandas_data_frame.concat([without_cve_file1, without_cve_file2], join="outer", ignore_index='true')

# combained the results of with cve and without cve
final_result = pandas_data_frame.concat([merged_cve_values, merged_non_cve_values], join="outer", ignore_index='true')

# # writing to Excel
datatoexcel = pandas_data_frame.ExcelWriter('out.xlsx')
 
# # write file1 to excel
final_result.to_excel(datatoexcel)
 
# # save the excel
datatoexcel.save()

# print("file1s Ittrated and stored to an Xlxs File")

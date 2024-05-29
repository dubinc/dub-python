# LeadsCities


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `city`                                                                         | *str*                                                                          | :heavy_check_mark:                                                             | The name of the city                                                           |
| `country`                                                                      | [components.LeadsCitiesCountry](../../models/components/leadscitiescountry.md) | :heavy_check_mark:                                                             | The 2-letter country code of the city: https://d.to/geo                        |
| `leads`                                                                        | *float*                                                                        | :heavy_check_mark:                                                             | The number of leads from this city                                             |
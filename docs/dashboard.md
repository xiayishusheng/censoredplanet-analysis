# Dashboard

The dashboard uses the [merged reduced table](./merged_reduced_scans_table.md) to display censorship data in a fast and navigable way.

## Important Definitions

### Stages and Outcomes

The `outcome` dropdown in the dashboard consists of strings of the format `stage/outcome`. For more documentation on stages and outcomes please read the documentation [here](./merged_reduced_scans_table.md#outcome-classification)

### Unexpected Outcome

Counts and ratios of unexpected outcomes are calculated in the dashboard to help users find domains and networks with possible censorship activity.

#### Outcomes considered expected

- `complete/success` This means the test ran fully and gave an expected response (matching the control response).

This means that the connection completed as expected with no interference.

#### Outcomes considered unexpected

Highly indicative of censorship:

- `content/blockpage' This means the test saw a known blockpage response, which is a strong indication censorship.

Potentially indicative of censorship:

- Protocol errors, especially `timeout` or `tcp/reset`. Inserting or dropping packets in ways that cause protocol errors is a common censorsihp technique. However protocol errors can also be caused by internet outages or poorly performing networks. To determine whether a protocol error is likely censorship look at the data over time and see if you can find a point where the outcome changed abruptly. If there was always a low level of protocol errors then it's more likely to be ppoor network conditions, whereas an abrupt change is more likely to show a change in censor behavior.
- Content mismatch errors in Echo and Discard.

Less indicative of censorship:

- Content mismatch errors:

These outcomes are all counted as unexpected and affect the unexpected ratio in a negative way.

#### Outcomes considered invalid

- Any outcome in the `setup/` or `dial/` stages. These tests didn't make it far enough to send the part of the connection (like the domain name) that would trigger censorship.
- Any `/invalid` outcome. These outcomes usually represent tests that are invalid for testing system reasons.
- `template_mismatch` This outcome means that the

These outcomes are not counted at all toward the ratios in a positive or negative way.

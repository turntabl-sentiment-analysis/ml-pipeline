import sys

from great_expectations import DataContext

# checkpoint configuration
context = DataContext("kerdo_project/great_expectations")
checkpoint = context.get_checkpoint("sentiment_analysis_checkpoint")

# load batches of data
batches_to_validate = []
for batch in checkpoint["batches"]:
  batch_kwargs = batch["batch_kwargs"]
  for suite_name in batch["sentiment_analysis_suite"]:
      suite = context.get_expectation_suite(suite_name)
      batch = context.get_batch(batch_kwargs, suite)
      batches_to_validate.append(batch)

# run the validation operator
results = context.run_validation_operator(
  checkpoint["sentiment_analysis_checkpoint"],
  assets_to_validate=batches_to_validate,
  # TODO prepare for new RunID - checkpoint name and timestamp
  # run_id=RunID(checkpoint)
)

# take action based on results
if not results["success"]:
  print("Validation failed!")
  sys.exit(1)

print("Validation succeeded!")
sys.exit(0)
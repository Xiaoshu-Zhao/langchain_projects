## Key Methods

- invoke/ainvoke  : Transforms a single input into an output.
- batch/abatch: Efficiently transforms multiple inputs into outputs.
- stream/astream: Streams output from a single input as it's produced.
- astream_log: Streams output and selected intermediate results froan input.

### Invoke:

- core abstract method and any class that inherit `Runnable` have to implement.
- accept `RunnableConfig` as an optional input

### batch:

- create a thread pool and concurrently call `invoke` function.
- `Langchain`  has it is own thread pool, which keep the same context when create a new thread
- the thread pool will be killed when the `batch` function finish.

## Related Knowledge

### python Generic

- define input and output type by following code:

```python
Input = TypeVar("Input", contravariant=True)
# Output type should implement __concat__, as eg str, list, dict do
Output = TypeVar("Output", covariant=True)

class Runnable(Generic[Input, Output], ABC):
```

- made code more clear and readable
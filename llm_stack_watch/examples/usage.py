from llm_stack_watch import Config, OpenAIProvider

def main():
    # Initialize configuration
    config = Config(
        api_key="your-logging-api-key",
        logging_url="https://your-logging-endpoint.com/logs",
        enable_logging=True
    )
    
    # Initialize provider
    provider = OpenAIProvider(
        model="gpt-3.5-turbo",
        config=config,
        api_key="your-openai-api-key"
    )
    
    # Create messages
    messages = [
        {"role": "user", "content": "Hello, how are you?"}
    ]
    
    # Method 1: Manual tracing
    trace = provider.trace(
        user_id="user123",
        label="chat_completion",
        meta_data={"session_id": "session456"}
    )
    
    response = provider.chat(messages)
    trace.end(response, messages)
    
    # Method 2: Context manager (automatically handles errors)
    with provider.trace(user_id="user123", label="chat_with_context") as trace:
        response = provider.chat(messages)
        trace.end(response, messages)
    
    print("Chat completed and logged!")

if __name__ == "__main__":
    main()
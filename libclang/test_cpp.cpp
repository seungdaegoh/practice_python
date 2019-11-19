cass TextComponent
{
    public:
        TextComponent();

        std::string text() const;
        void setText(const std::string& value);

        void superSecretFunction();

    private:
        std::string m_text;
};
